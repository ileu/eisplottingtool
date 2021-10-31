import os
import re

import Base


def main():
    file1 = r"Test1.mpr"
    file2 = r"Test2.mpr"

    peis_mpr_files = [file1, file2]
    fig, ax = Base.create_fig()
    extra_time = 0
    for file in peis_mpr_files:
        image_name = '_'.join(re.split("[_.]", file)[-5:-1])
        print(file, image_name)
        data = Base.load_data(file)
        print("Cycles: ", len(data))
        print(f"Time: {extra_time}")
        start_time = data[0].df['time/s'][0]
        for i, cycle in enumerate(data):
            cycle.mark_points = []
            cycle.df['time/s'] += extra_time- start_time
            cycle.plot_lifecycle(ax)
            # time = cycle['time/s'] / 3600.0 - cycle['time/s'].iloc[0] / 3600.0
            # ax.plot(time, cycle['Ns'], color='blue')
            # ax.plot(time, cycle['I/mA'] * 1e3 / 7.0, color='red')
            print(f"cycle {i}")

            print(
                    f"start {cycle['time/s'].iloc[0] / 3600.0}, end {cycle['time/s'].iloc[-1] / 3600.0}"
                    )
        # lim = .07
        # ax.set_ylim(-lim, lim)
        extra_time = data[-1].df['time/s'].iloc[-1]

    Base.save_fig(
            os.path.join(
                    os.path.dirname(file), "plots", f"life.png"

                    )
            )


if __name__ == "__main__":
    print("start")
    main()
    print("end")
