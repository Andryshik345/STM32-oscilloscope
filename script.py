import sys, os, time, serial
import matplotlib.pyplot as plt

# Plot the graph
def draw_plot(x, y, ax):
    plt.cla()
    ax.plot(x, y)
    plt.pause(1)
    
# Format the inpur into co-ordinates arrays
def format_lines_and_draw(lines, ax):
    x, y = [], []
    for line in lines:
        line = str(line)
        if not '#' in line and not '\n' in line:
            x.append(float(line[2:].split('|')[0]))
            y.append(float(line[2:].split('|')[1]))
        else:
            x.append(0.0)
            y.append(0.0)
    draw_plot(x[100:2500], y[100:2500], ax)
    
# Read the data from STM32
def read_serial(ser, ax):
    ser.write(b's\n')
    ser.flush()
    lines = []
    while True:
        s = str(ser.readline())
        if len(s) <= 3:
            break
        else:
            lines.append(s)
    format_lines_and_draw(lines, ax)

def main():
    ser = serial.Serial('COM5', timeout=1)
    fig, ax = plt.subplots()
    fig.show()
    while True:
        s = read_serial(ser, ax)

if __name__ == '__main__':
    main()