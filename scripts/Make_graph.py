import matplotlib.pyplot as plot
import numpy as np
import Read_csv

#x軸の最大値として起用するトータルゲーム数を代入
Glaph_limit = Read_csv.TotalGameCount

#x軸の横軸を指定
x = np.arange( 0, Glaph_limit, Glaph_limit/10 )

y = [2 * x]

#plt.plot(x, y)
#plt.show()
