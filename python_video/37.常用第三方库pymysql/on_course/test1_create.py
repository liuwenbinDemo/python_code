from . import get_conn


def test_create():
    # 建立连接
    conn = get_conn()

    # 获取游标
    cursor = conn.cursor()

    # sql语句
    sql = """
    CREATE TABLE `testcase` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `title` varchar(255) COLLATE utf8_bin NOT NULL,
    `expect` varchar(255) COLLATE utf8_bin NOT NULL,
    `owner` varchar(255) COLLATE utf8_bin NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
    """

    # 执行SQL
    cursor.execute(sql)

    # 关闭连接
    conn.close()


