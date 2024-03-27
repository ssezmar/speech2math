import matplotlib.pyplot as plt

def show_formula(formula, filename):
    plt.text(0.5, 0.5, formula, fontsize=20, ha='center', va='center')
    plt.axis('off')
    plt.savefig(filename, bbox_inches='tight')
    plt.close()



