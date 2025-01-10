import numpy as np

def fractal_dimension(binary_img):
    # Box sizes to test (smaller boxes capture more detail)
    sizes = [2, 4, 8, 16, 32, 64]
    counts = []

    # Loop over each box size
    for size in sizes:
        count = 0
        # Divide the image into boxes of the current size
        for i in range(0, binary_img.shape[0], size):
            for j in range(0, binary_img.shape[1], size):
                # Check if the box contains any non-zero pixels
                if np.any(binary_img[i:i+size, j:j+size]):
                    count += 1
        # Store the number of filled boxes for this size
        counts.append(count)
    
    # Calculate the logarithm of box sizes and counts
    log_sizes = np.log(sizes)
    log_counts = np.log(counts)
    
    # Fit a line to the log-log data and find the slope
    slope, _ = np.polyfit(log_sizes, log_counts, 1)
    
    # Return the fractal dimension (negative slope)
    return -slope
