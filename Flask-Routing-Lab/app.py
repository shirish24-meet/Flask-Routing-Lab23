from flask import Flask, redirect, request, render_template, url_for


app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)

# Your code should be below

@app.route('/')
def home():
	return render_template("/home.html")

@app.route('/handbag')
def handbag():
	return render_template("/handbag.html")

@app.route('/clothbag')
def clothbag():
	return render_template("/clothbag.html")

@app.route('/luggage')
def luggage():
	return render_template("/luggage.html")

@app.route('/product')
def product():
	return render_template("/product.html")

@app.route('/cart')
def cart():
	return render_template("/cart.html")

# Your code should be above

if __name__ == "__main__":  # Makes sure this is the main process
    app.run(debug=True)