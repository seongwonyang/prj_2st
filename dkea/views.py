from django.shortcuts import render, get_object_or_404
# Bookmark 테이블의 데이터를 가져오기 위해 models.py에서 Bookmark 클래스를 import
from .models import Category, Product
from django.db import connection

# Create your views here.
def DkeaMain(request):
    try:
        cursor = connection.cursor()

        strSql = "SELECT distinct c_code,c_name"
        strSql+= " FROM dkea.dkea_category"
        result = cursor.execute(strSql)
        datas = cursor.fetchall()

        connection.commit()
        connection.close()

        main = []
        for data in datas:
            row = {'c_code': data[0],
                   'c_name': data[1]
                   }

            main.append(row)

    except:
        connection.rollback()
        print("Failed selecting in DkeaMain")

    return render(request, 'main.html', {'main': main})


def DkeaListView(request, list):
    try:
        cursor = connection.cursor()

        strSql = "SELECT dkea.dkea_category.c_code,dkea.dkea_category.c_name,dkea.dkea_product.img_src,dkea.dkea_product.p_name, dkea.dkea_product.p_id"
        strSql += " FROM dkea.dkea_product"
        strSql += " LEFT OUTER JOIN dkea.dkea_category on dkea_category.c_id=dkea_product.c_id WHERE dkea.dkea_category.c_code = (%s)"

        result = cursor.execute(strSql, (list,))
        datas = cursor.fetchall()

        str_cname = "SELECT distinct dkea.dkea_category.c_name"
        str_cname += " FROM dkea.dkea_category"
        str_cname += " WHERE dkea.dkea_category.c_code = (%s)"

        result2 = cursor.execute(str_cname, (list,))
        datas2 = cursor.fetchall()

        connection.commit()
        connection.close()

        cate_cname = datas2[0][0]

        cate = []
        for data in datas:
            row = {'c_code': data[0],
                   'c_name': data[1],
                   'img_src': data[2],
                   'p_name': data[3],
                   'p_id': data[4]}

            cate.append(row)

    except:
        connection.rollback()
        print("Failed selecting in DkeaListView")

    return render(request, 'category.html', {'cate': cate, 'cate_cname': cate_cname})


def DkeaDetailView(request, detail):
    try:
        cursor = connection.cursor()

        strSql = "SELECT dkea.dkea_category.c_id,dkea.dkea_category.i_name ,dkea.dkea_category.c_name ,dkea.dkea_product.link ,dkea.dkea_product.p_id ,dkea.dkea_product.p_name ,dkea.dkea_product.price"
        strSql += " FROM dkea.dkea_product"
        strSql += " LEFT OUTER JOIN dkea.dkea_category on dkea_category.c_id=dkea_product.c_id WHERE dkea.dkea_product.p_id = (%s)"

        result = cursor.execute(strSql, (detail,))
        datas = cursor.fetchall()

        connection.commit()
        connection.close()

        pro = {'c_id': datas[0][0],
                'i_name': datas[0][1],
                'c_name': datas[0][2],
                'link': datas[0][3],
                'p_id': datas[0][4],
                'p_name': datas[0][5],
                'p_price': datas[0][6]}

    except:
        connection.rollback()
        print("Failed selecting in DkeaDetailView")

    return render(request, 'product.html', {'pro':pro})

