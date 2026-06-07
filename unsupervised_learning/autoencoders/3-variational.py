#!/usr/bin/env python3
""" variational autoencoder """
import tensorflow.keras as keras


def autoencoder(input_dims, hidden_layers, latent_dims):
    """
    ARGS:
        -input_dims {integer}: containing the dimensions of the model input
        -hidden_layers {list}: containing the number of nodes
            for each hidden layer in the encoder, respectively
        -latent_dims {integer}: containing the dimensions
            of the latent space representation

    Returns: encoder, decoder, auto
        -encoder is the encoder model
        -decoder is the decoder model
        -auto is the full autoencoder model
    """

    """ Encoder """
    input_encoder = keras.Input(shape=(input_dims,))

    encode = input_encoder
    for i in range(len(hidden_layers)):
        encode = keras.layers.Dense(hidden_layers[i],
                                    activation='relu')(encode)

    z_mean = keras.layers.Dense(latent_dims)(encode)
    z_log_sigma = keras.layers.Dense(latent_dims)(encode)

    def sampling(z):
        """sampling a new points"""
        z_mean, z_log_sigma = z
        batch = keras.backend.shape(z_mean)[0]
        dims = keras.backend.int_shape(z_mean)[1]
        epsilon = keras.backend.random_normal(shape=(batch, dims))
        return z_mean + keras.backend.exp(z_log_sigma / 2) * epsilon

    z = keras.layers.Lambda(sampling)([z_mean, z_log_sigma])
    
    encoder = keras.Model(inputs=input_encoder,
                          outputs=[z, z_mean, z_log_sigma])

    """ Decoder """
    input_decoder = keras.Input(shape=(latent_dims, ))

    decode = input_decoder
    for j in range(len(hidden_layers)-1, -1, -1):
        decode = keras.layers.Dense(hidden_layers[j],
                                    activation='relu')(decode)

    # Decoder output
    decode = keras.layers.Dense(input_dims,
                                activation='sigmoid')(decode)

    decoder = keras.Model(inputs=input_decoder, outputs=decode)

    """ VAE Link and Custom Loss """
    # Get only the sampled 'z' output from the encoder to feed the decoder
    encoder_outputs = encoder(input_encoder)
    z_sampled = encoder_outputs[0]
    outputs = decoder(z_sampled)
    
    vae = keras.Model(input_encoder, outputs)

    def loss(true, pred):
        # Compute reconstruction loss using the correct runtime arguments
        reconstruction_loss = keras.losses.binary_crossentropy(true, pred)
        reconstruction_loss *= input_dims
        
        # Compute KL divergence loss
        kl_loss = 1 + z_log_sigma - keras.backend.square(z_mean) -\
            keras.backend.exp(z_log_sigma)
        kl_loss = keras.backend.sum(kl_loss, axis=-1)
        kl_loss *= -0.5
        
        return keras.backend.mean(reconstruction_loss + kl_loss)

    vae.compile(optimizer='adam', loss=loss)
    return encoder, decoder, vae
