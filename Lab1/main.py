from storage_manager import StorageManager

def main():
    storage_manager = StorageManager.get_instance()

    storage_manager.set_user_storage("user1", "local")
    user1_storage = storage_manager.get_user_storage("user1")
    user1_storage.upload_file("file1.txt")
    user1_storage.download_file("file1.txt")

    storage_manager.set_user_storage("user2", "s3")
    user2_storage = storage_manager.get_user_storage("user2")
    user2_storage.upload_file("file2.txt")
    user2_storage.download_file("file2.txt")

if __name__ == "__main__":
    main()
