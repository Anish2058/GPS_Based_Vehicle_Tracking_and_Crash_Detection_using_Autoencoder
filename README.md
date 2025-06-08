GPS-Based Vehicle Tracking & Crash Detection System

This project enhances road safety through real-time vehicle monitoring and crash detection using a Raspberry Pi-based system with GPS and an accelerometer.
Overview

    Location Tracking: Uses GPS to monitor vehicle movement in real time.

    Crash Detection: Uses deep learning models (GRUs and Autoencoders) to detect abnormal driving patterns.

    Anomaly Detection: Trained on normal driving data instead of crash datasets. Detects anomalies based on reconstruction error from accelerometer time-series data.

    Emergency Alerts: Sends alerts and live location using an internet connection if an anomaly (potential crash) is detected.

Model Performance

    Threshold MAE = 2.5 → F1 Score: 0.835

    Threshold MAE = 3.0 → F1 Score: 0.837

Tech Stack

    Hardware: Raspberry Pi, GPS module, Accelerometer

    Software: Python, TensorFlow/Keras (GRU + Autoencoder)

    Communication: Internet for real-time alerts and location sharing

Goal

To create a low-cost, intelligent system that promotes safer driving by detecting possible crashes and enabling timely emergency responses.
