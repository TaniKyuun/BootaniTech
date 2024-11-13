from flask import render_template, request, redirect, url_for
from flask import Blueprint
from flask_login import login_required
import numpy as np


bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    """Render Website Landing Page."""
    return render_template("index.html")


# only accessible to logged in users
@bp.route("/dashboard")
@login_required
def dashboard():
    """Render Website Dashboard Page."""
    return render_template("main/dashboard.html")


@bp.route("/submit_sample", methods=["GET", "POST"])
@login_required
def submit():
    return render_template("main/process.html")


# @bp.route("/submit_sample", methods=["GET", "POST"])
# @login_required
# def submit():
#     output_image = None
#     if request.method == "POST":
#         if "image" not in request.files:
#             return redirect(request.url)

#         file = request.files["image"]
#         model_name = request.form["model"]

#         # Specify the path to the model file
#         model_path = os.path.join(current_app.root_path, "models", model_name)

#         # Load the model
#         model = load_model(model_path)

#         # Preprocess the image
#         img = image.load_img(file, target_size=(224, 224))
#         x = image.img_to_array(img)
#         x = np.expand_dims(x, axis=0)

#         # Process the image
#         preds = model.predict(x)

#         # Save the processed image
#         output_image = "output.png"
#         # TODO: Save the processed image to output_filename

#     # Render the template with the output image
#     return render_template("main/process.html", output_image=output_image)
