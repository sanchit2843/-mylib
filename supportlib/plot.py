def data_plot(n_figures , data , encoder = None ,inv_normalize = None):
    n_row = int(n_figures/3)
    fig,axes = plt.subplots(figsize=(14, 10), nrows = n_row, ncols=3)
    for ax in axes.flatten():
        a = random.randint(0,len(data))
        (image,label) = data[a]
        label = int(label)
        if encoder:
            label = encoder[label]
        if inv_normalize:
            image = inv_normalize(image)
        image = image.numpy().transpose(1,2,0)
        im = ax.imshow(image)
        ax.set_title(label)
        ax.axis('off')
    plt.show()
def error_plot(dis_loss, gen_loss):
    plt.figure(figsize=(10,5))
    plt.title("Generator and Discriminator Loss During Training")
    plt.plot(gen_loss,label="G")
    plt.plot(dis_loss,label="D")
    plt.xlabel("epochs")
    plt.ylabel("Loss")
    plt.legend()
    plt.show()
