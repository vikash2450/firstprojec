import matplotlib.pyplot as plt

import numpy as np

labels = ['python','aws','devops','docker','kubernetes']

num_len = len(labels)

my_skills = [8,9,7,6,5]
closs_value = my_skills + [my_skills[0]]

angles = np.linspace(0,2 * np.pi,num_len,endpoint= False).tolist()

angles += angles[:1]  #complete the loop

fig, ax = plt.subplots(figsize=(6,6), subplot_kw=dict(polar=True))

ax.plot(angles,closs_value,color='blue',linewidth=2)
ax.fill(angles,closs_value,color='red',alpha=1)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels)
ax.set_yticks([2,4,6,8,10])
ax.set_yticklabels(['2','4','6','8','10'])
ax.set_title('my skills in programming language')
plt.show()



