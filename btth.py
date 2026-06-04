blood_inventory = [
    "BL001-Nguyen Van A-O+-250-31/12/2026",
    "BL002-Tran Thi B-A--350-15/11/2026",
    "BL003-Le Van C-AB+-250-20/10/2026"
]


def find_blood_bag_index(inventory, bag_id):
    for blood_bag in inventory:
        info = blood_bag.split("-")

        if info[0] == bag_id:
            return inventory.index(blood_bag)

    return -1


def bag_id_process():
    while True:
        bag_id = input(
            "Nhập mã túi máu mới: "
        ).strip().upper()

        if bag_id == "":
            print("Lỗi: Mã túi máu không được để trống!")
            continue

        return bag_id


def donor_name_process():
    while True:
        name = input(
            "Nhập tên người hiến: "
        ).strip().title()

        if name == "":
            print("Lỗi: Tên người hiến không được để trống!")
            continue

        return name


def blood_type_process():
    while True:
        blood_type = input(
            "Nhập nhóm máu: "
        ).strip().upper()

        if blood_type == "":
            print("Lỗi: Nhóm máu không được để trống!")
            continue

        return blood_type


def volume_process():
    while True:
        volume = input(
            "Nhập thể tích (ml): "
        ).strip()

        if not volume.isdigit():
            print("Lỗi: Thể tích phải là số nguyên lớn hơn 0!")
            continue

        volume = int(volume)

        if volume <= 0:
            print("Lỗi: Thể tích phải là số nguyên lớn hơn 0!")
            continue

        return str(volume)


def expiry_process(message="Nhập ngày hết hạn (DD/MM/YYYY): "):
    while True:
        expiry = input(message).strip()

        if expiry == "":
            print("Ngày hết hạn không được để trống!")
            continue

        return expiry


def display_inventory(inventory):
    if len(inventory) == 0:
        print("Kho máu hiện chưa có túi máu nào.")
        return

    total_volume = 0

    print("\n----- DANH SÁCH TÚI MÁU TRONG KHO -----")

    for i, blood_bag in enumerate(inventory, start=1):
        info = blood_bag.split("-")

        total_volume += int(info[3])

        print(
            f"{i}. "
            f"[{info[0]}] "
            f"{info[1]:<20} | "
            f"Nhóm máu: {info[2]:<4} | "
            f"Thể tích: {info[3]:<4} ml | "
            f"HSD: {info[4]}"
        )

    print(f"\nTổng thể tích máu trong kho: {total_volume} ml")


def add_blood_bag(inventory):
    print("\n--- NHẬP TÚI MÁU MỚI ---")

    bag_id = bag_id_process()

    index = find_blood_bag_index(
        inventory,
        bag_id
    )

    if index != -1:
        print(
            f"Lỗi: Mã túi máu {bag_id} đã tồn tại! "
            f"Vui lòng nhập mã khác."
        )
        return

    donor_name = donor_name_process()
    blood_type = blood_type_process()
    volume = volume_process()
    expiry = expiry_process()

    new_blood_bag = "-".join([
        bag_id,
        donor_name,
        blood_type,
        volume,
        expiry
    ])

    inventory.append(new_blood_bag)

    print(
        f"\nThành công: Đã nhập túi máu {bag_id} vào kho!"
    )

    print("\nSau khi chuẩn hóa, dữ liệu được lưu vào list là:")
    print(new_blood_bag)


def update_expiry(inventory):
    print("\n--- GIA HẠN / SỬA NGÀY HẾT HẠN ---")

    bag_id = input(
        "Nhập mã túi máu cần cập nhật: "
    ).strip().upper()

    if bag_id == "":
        print("Lỗi: Mã túi máu không được để trống!")
        return

    index = find_blood_bag_index(
        inventory,
        bag_id
    )

    if index == -1:
        print(
            f"Lỗi: Không tìm thấy túi máu "
            f"{bag_id} trong kho!"
        )
        return

    info = inventory[index].split("-")

    new_expiry = expiry_process(
        "Nhập ngày hết hạn mới: "
    )

    info[4] = new_expiry

    inventory[index] = "-".join(info)

    print(
        f"\nThành công: Đã cập nhật ngày hết hạn "
        f"cho túi máu {bag_id}!"
    )


def remove_blood_bag(inventory):
    print("\n--- XUẤT / HỦY TÚI MÁU ---")

    bag_id = input(
        "Nhập mã túi máu cần xuất/hủy: "
    ).strip().upper()

    if bag_id == "":
        print("Lỗi: Mã túi máu không được để trống!")
        return

    index = find_blood_bag_index(
        inventory,
        bag_id
    )

    if index == -1:
        print(
            f"Lỗi: Không tìm thấy túi máu "
            f"{bag_id} trong kho!"
        )
        return

    inventory.pop(index)

    print(
        f"\nThành công: Đã xuất túi máu "
        f"{bag_id} khỏi kho!"
    )


def main():
    while True:
        choice = input("""
=== HỆ THỐNG QUẢN LÝ KHO MÁU RIKKEI ===

1. Xem danh sách túi máu trong kho
2. Nhập túi máu mới
3. Gia hạn / Sửa ngày hết hạn
4. Xuất / Hủy túi máu
5. Thoát chương trình

========================================
Chọn chức năng (1-5):
""").strip()

        if choice == "1":
            display_inventory(blood_inventory)

        elif choice == "2":
            add_blood_bag(blood_inventory)

        elif choice == "3":
            update_expiry(blood_inventory)

        elif choice == "4":
            remove_blood_bag(blood_inventory)

        elif choice == "5":
            print(
                "Cảm ơn bác sĩ đã sử dụng hệ thống. "
                "Hẹn gặp lại!"
            )
            break

        else:
            print(
                "Lựa chọn không hợp lệ, "
                "vui lòng nhập số từ 1-5!"
            )


if __name__ == "__main__":
    main()