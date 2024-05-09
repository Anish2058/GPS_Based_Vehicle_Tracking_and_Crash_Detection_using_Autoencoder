GPS-Based Vehicle Tracking and Accelerometer-driven Crash Detection presents a
solution for enhancing road safety through real-time vehicle monitoring and crash
detection using a Raspberry Pi-based system. Using components such as GPS and an
accelerometer, the system tracks vehicle location and detects potential accidents. Deep
Learning techniques Gated Recurrent Units (GRUs) and Autoencoders are used to train
the model using the dataset of accelerometer under normal driving condition instead of
training the model on crash dataset which are comparatively more difficult to obtain. By
training on normal driving scenarios, the system detects the anomalous data obtained
from accelerometer while driving. The time series data obtained from accelerometer is
reconstructed by the model according to the pattern it learnt from the training dataset.
The anomaly is detected based on the error between input time series data and the
reconstructed data. A threshold Mean Absolute Error is set above which the data is
considered to be an anomaly. Keeping the threshold error 2.5, the model achieved an F1
score of 0.835 and with threshold error 3, F1 score was 0.837. The system utilizes
internet connection for emergency alerts and location sharing. Overall, this project aims
to contribute to a safer driving environment by providing a reliable and efficient
solution.
