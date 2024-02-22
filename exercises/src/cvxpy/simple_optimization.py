#%%
import matplotlib.pyplot as plt
import numpy as np
import cvxpy as cvx

def plot_equation(xr, yr):
    '''
        Function for plotting the equation
    '''
    x = np.linspace(-5, 5, 100)
    y = (x - 1) ** 2 + 1

    # plot the curve
    plt.plot(x, y)

    # mark the constrained part
    plt.axvspan(-5, 0, color='blue', alpha=0.2)

    # mark the optmization value
    plt.plot(xr, yr, 'ro')
    
    # add labels and title
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('$(x-1)^2 + 1$')

    plt.show()

def solve_convex_optimization():
    try:
        x = cvx.Variable(1)
        objective = cvx.Minimize((x - 1)**2 + 1)
        constraints = [x <= 0]
        problem = cvx.Problem(objective, constraints)
        result = problem.solve()
        
        print('Result: ', problem.status)
        print(f'Optimal value of x: {x.value[0]:6f}')
        print('Optimal value of the objective: {:.6f}'.format(problem.value))

        return x.value[0], problem.value

    except BaseException as err:
        print('Error: ', err)

if __name__ == '__main__':
    result = solve_convex_optimization()
    plot_equation(result[0], result[1])
    
# %%
