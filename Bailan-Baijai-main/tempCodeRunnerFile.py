@app.get("/chanels",tags=["Money"])
async def show_payment_method()->dict:
    return {"chanels":controller.show_payment_method()}