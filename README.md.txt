# 🧠 Cloud-Based Robotics Vision Simulation (PyBullet + ROS)

This project showcases two core robotics vision tasks—**shape classification** and **vision-guided autonomous navigation**—implemented fully in cloud environments using **PyBullet**, **ROS**, **OpenCV**, and **TheConstruct.ai**. It demonstrates both **passive perception** (understanding images) and **active perception** (using vision to act in real-time).

---

## 📌 Project Overview

This project consists of two major tasks:

### **🔹 Task 1: Robot Vision Simulation in PyBullet**

* Created geometric objects (cube, sphere, cylinder, pyramid) using **URDF**.
* Built a synthetic 3D environment and captured RGB images using virtual cameras.
* Preprocessed images (resize, normalize).
* Used a pretrained **MobileNetV2** CNN for shape classification.
* Evaluated model performance with a confusion matrix and accuracy metrics.

**Tools Used:** PyBullet, Python, MobileNetV2, OpenCV, Matplotlib, Google Colab.

---

### **🔹 Task 2: Vision-Guided Autonomous Navigation in ROS**

* Used a **TurtleBot3** robot in a cloud ROS environment (TheConstruct.ai).
* Implemented real-time **red-object detection** using OpenCV (HSV thresholding).
* Created a custom ROS package `vision_nav` with node `color_tracker.py`.
* Robot behavior:

  * Rotate left/right depending on object position
  * Move forward when aligned
  * Stop if no object detected
* Achieved full closed-loop perception-to-action navigation.

**Tools Used:** ROS Noetic, Gazebo, OpenCV, cv_bridge, geometry_msgs, sensor_msgs.

---

## 📂 Repository Structure

```
cloud-robotics-vision-simulation/
│
├── README.md
│
├── task1_pybullet/
│   ├── urdf/
│   ├── simulation_code.ipynb
│
├── task2_ros_navigation/
│   ├── vision_nav/
│   │   └── color_tracker.py
│   └── screenshots/
│
├── reports/
│   └── ARACV_Assignment.pdf
│
```

---

## 📊 Task 1 Results (PyBullet)

* Multiple camera views captured (diagonal, top-down, close-up).
* MobileNetV2 classification accuracy ~18% (expected due to ImageNet mismatch).
* Confusion matrix analysis revealed shape misclassifications and feature overlap.

**Key Insight:** Pretrained models struggle on synthetic geometric shapes without fine-tuning.

---

## 🤖 Task 2 Results (ROS Navigation)

* Real-time tracking of a red object using HSV segmentation.
* TurtleBot3 successfully aligned and navigated toward the target.
* Demonstrated a complete **sense → process → act** pipeline.

**Limitations:**

* Hardcoded HSV values
* No obstacle avoidance
* No smoothing/filtering

**Potential Improvements:**

* Dynamic thresholding or learned detectors (YOLO, SSD)
* LIDAR-based collision avoidance
* Kalman filtering for smoother tracking
* Proportional control for smooth motion

---

## 🔗 Important Links

* **Task 1 (PyBullet) – Google Colab:**
  [https://colab.research.google.com/drive/1en0lSX-WQLqjc4s24X8FXwSsgRO5RF6_?usp=sharing](https://colab.research.google.com/drive/1en0lSX-WQLqjc4s24X8FXwSsgRO5RF6_?usp=sharing)

* **Task 2 (ROS Navigation) – ROSject:**
  *Unique ID:* FVEFV0AASI

* **Backup Files:**
  [https://drive.google.com/drive/folders/11p4VZ7Dq13C2X_Ce4knErTA_Q9aBdXZt?usp=sharing](https://drive.google.com/drive/folders/11p4VZ7Dq13C2X_Ce4knErTA_Q9aBdXZt?usp=sharing)

---

## 🛠️ Technologies Used

* **PyBullet** (Vision simulation)
* **ROS Noetic + Gazebo** (Autonomous navigation)
* **OpenCV** (Image processing)
* **MobileNetV2 + PyTorch** (Deep learning)
* **Python 3.11**
* **TheConstruct.ai** (Cloud-based simulation)
* **Google Colab**

---

## 👨‍💻 Author

**Gaurav Arun**
MSc Artificial Intelligence – Robotics, Automation & Computer Vision
2025


