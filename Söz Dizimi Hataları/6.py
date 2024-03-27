import tensorflow  tf

model = tf.keras.Sequential(
  tf.keras.layers.Dense(64, activation="relu", input_shape=(10,)),
  tf.keras.layers.Dense(64, activation="relu"),
  tf.keras.layers.Dense(1)
])

model.compile(optimizer=tf.keras.optimizers.Adam(0.01),
              loss="mse",
              metrics=["mae"])

model.fit(x_train, y_train, epochs=10)