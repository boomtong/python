import os
import multiprocessing

def copy_file(filename, old_folder_name, new_folder_name):
    """完成文件的复制"""
    print("=======>模拟拷贝文件： 从%s----->%s 文件名是%s"  %(old_folder_name, new_folder_name, filename))
    old_f = open(old_folder_name + "/" + filename, "rb")
    content = old_f.read()
    old_f.close()

    new_f = open(new_folder_name + "/" + filename, "wb")
    new_f.write(content)
    new_f.close()


def main():
    # 1.获取用户要copy的文件夹的名字
    old_folder_name = input("请输入要copy的文件夹的名字：")

    # 2.创建一个新的文件夹
    try:
        new_folder_name = old_folder_name + "附件"
        os.mkdir(new_folder_name)
    except:
        pass

    # 3. 获取文件夹的所有待拷贝的文件名字   listdir()
    filenames = os.listdir(old_folder_name)
    print(filenames)

    # 4. 创建进程池
    po = multiprocessing.Pool(5)

    # 5. 像进程池中添加copy文件的任务
    for filename in filenames:
        po.apply_async(copy_file, args=(filename, old_folder_name, new_folder_name))

    po.close()
    po.join()


if __name__ == "__main":
    main()