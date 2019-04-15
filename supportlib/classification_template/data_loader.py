class dog_dataset(Dataset):
  def __init__(self,image_dir,transform = None):

    self.img_dir = image_dir
    self.transform = transform
    self.id = os.listdir(self.img_dir)
  def __len__(self):
    return len(os.listdir(self.img_dir))
  def __getitem__(self,idx):
    img_name = os.path.join(self.img_dir, self.id[idx])
    image = cv2.imread(img_name)
    if self.transform:
      image = self.transform(image)
    return image
