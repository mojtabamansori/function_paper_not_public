def change_sample(xdata, label, subIdx, n_new_time,overlap):
    n_time = 3

    new_shape_1 = int(xdata.shape[0] * (n_time / n_new_time))
    new_shape_2 = int(xdata.shape[1])
    new_shape_3 = int(xdata.shape[2] * (n_new_time / n_time))

    xdata_new = np.zeros((new_shape_1, new_shape_2, new_shape_3))
    subIdx_new = np.zeros((new_shape_1, 1))
    label_new = np.zeros((new_shape_1, 1))

    # xdata, label, subIdx = change_sample(xdata, label, subIdx, n_new_time)
    if overlap==0:
        for step in range(0, len(xdata_new), int(n_time / n_new_time)):
            n_step = range(int(n_time / n_new_time))
            for i in n_step:
                xdata_new[step + i, :, :] = xdata[int(step / (n_time / n_new_time)),
                                            :, (new_shape_3 * i):(new_shape_3 * (i + 1))]
                label_new[step + i, 0] = label[int(step / (n_time / n_new_time))]
                subIdx_new[step + i, 0] = subIdx[int(step / (n_time / n_new_time))]
    if overlap==1:
        if n_new_time == 2:
            for step in range(0, len(xdata_new), int(n_time / n_new_time)):
                n_step = range(int(n_time / n_new_time))
                for i in n_step:
                    xdata_new[step + i, :, :] = xdata[int(step / (n_time / n_new_time)),
                                                :, (new_shape_3 * i):(new_shape_3 * (i + 1))]
                    label_new[step + i, 0] = label[int(step / (n_time / n_new_time))]
                    subIdx_new[step + i, 0] = subIdx[int(step / (n_time / n_new_time))]
            for n_repeat in range(len(xdata_new)):
                if n_repeat>=2:
                    if (n_repeat//2) == 0:
                        xdata_new[n_repeat,:,:]= 0
                        label_new[:, 0] = 0
                        subIdx_new[:, 0] = 0


        xdata_new = np.delete(xdata_new,np.where(np.all(xdata_new == 0 ,axis=(1,2))),axis= 0)
        label_new = np.delete(label_new,np.where(np.all(xdata_new == 0 ,axis=(1,2))),axis= 0)
        subIdx_new = np.delete(subIdx_new,np.where(np.all(xdata_new == 0 ,axis=(1,2))),axis= 0)
    if overlap==1:
        if n_new_time == 1:
            for step in range(0, len(xdata_new), int(n_time / n_new_time)):
                n_step = range(int(n_time / n_new_time))
                for i in n_step:
                    xdata_new[step + i, :, :] = xdata[int(step / (n_time / n_new_time)),
                                                :, (new_shape_3 * i):(new_shape_3 * (i + 1))]
                    label_new[step + i, 0] = label[int(step / (n_time / n_new_time))]
                    subIdx_new[step + i, 0] = subIdx[int(step / (n_time / n_new_time))]
            for n_repeat in range(len(xdata_new)):
                if n_repeat>=2:
                    if (n_repeat//3) == 0:
                        xdata_new[n_repeat,:,:]= 0
                        label_new[:, 0] = 0
                        subIdx_new[:, 0] = 0
                    if ((n_repeat-1)//3) == 0:
                        xdata_new[n_repeat,:,:]= 0
                        label_new[:, 0] = 0
                        subIdx_new[:, 0] = 0



        xdata_new = np.delete(xdata_new,np.where(np.all(xdata_new == 0 ,axis=(1,2))),axis= 0)
        label_new = np.delete(label_new,np.where(np.all(xdata_new == 0 ,axis=(1,2))),axis= 0)
        subIdx_new = np.delete(subIdx_new,np.where(np.all(xdata_new == 0 ,axis=(1,2))),axis= 0)

    return xdata_new, label_new, subIdx_new
