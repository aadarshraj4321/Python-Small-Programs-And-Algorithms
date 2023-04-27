import tkinter as tk

class GSTCalculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("GST Calculator")
        
        # Create input fields
        self.price_label = tk.Label(self.window, text="Price:")
        self.price_label.grid(column=0, row=0)
        self.price_entry = tk.Entry(self.window)
        self.price_entry.grid(column=1, row=0)
        
        self.gst_label = tk.Label(self.window, text="GST %:")
        self.gst_label.grid(column=0, row=1)
        self.gst_entry = tk.Entry(self.window)
        self.gst_entry.grid(column=1, row=1)
        
        # Create calculate button
        self.calculate_button = tk.Button(self.window, text="Calculate", command=self.calculate_gst)
        self.calculate_button.grid(column=0, row=2)
        
        # Create output field
        self.total_label = tk.Label(self.window, text="Total Price (incl. GST):")
        self.total_label.grid(column=0, row=3)
        self.total_entry = tk.Entry(self.window, state="readonly")
        self.total_entry.grid(column=1, row=3)
        
        self.window.mainloop()
    
    def calculate_gst(self):
        price = float(self.price_entry.get())
        gst = float(self.gst_entry.get())
        
        # Calculate total price with GST
        total = price * (1 + (gst / 100))
        
        # Display total price
        self.total_entry.configure(state="normal")
        self.total_entry.delete(0, tk.END)
        self.total_entry.insert(0, "{:.2f}".format(total))
        self.total_entry.configure(state="readonly")

if __name__ == "__main__":
    calculator = GSTCalculator()
