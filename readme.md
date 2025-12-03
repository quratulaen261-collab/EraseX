# EraseX - AI Object Removal Tool

**EraseX** is a simple AI-powered tool that allows users to remove unwanted objects from any image. Using a drawing interface, you can highlight the object you want to erase, and the tool automatically removes it using OpenCV's inpainting algorithm.

---

## Features

* Upload any image in `jpg`, `jpeg`, or `png` format.
* Draw over the object you want to remove with an intuitive canvas interface.
* Automatically remove the selected object from the image.
* Preview the original and edited images side by side.
* Built using **Streamlit** for a user-friendly web interface.

---

## Demo Screenshot

*(Add a screenshot of your app here once you run it)*

---

## Installation

1. Clone the repository:

```bash
git clone <repository_url>
cd <repository_folder>
```

2. Create and activate a Python virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

**Dependencies include:**

* streamlit
* numpy
* opencv-python
* pillow
* streamlit-drawable-canvas

---

## Usage

1. Run the Streamlit app:

```bash
streamlit run app.py
```

2. Upload an image you want to edit.

3. Draw over the object you want to remove using the canvas.

4. Click the **"Remove Object"** button.

5. View the edited image with the object removed.

---

## How It Works

1. User uploads an image.
2. A canvas overlay allows the user to draw a mask over the object.
3. The mask is processed using OpenCV.
4. The `cv2.inpaint` function removes the object from the original image using the selected mask.
5. The resulting image is displayed.

---

## Screenshots

*(Optional: Add step-by-step screenshots showing upload, drawing mask, and result)*

---

## Notes

* The inpainting works best for relatively small objects or simple backgrounds.
* Large or complex objects may require more precise mask drawing for better results.
* Currently, only single object removal per edit is supported.

---

## License

This project is open-source and free to use for personal or educational purposes.
