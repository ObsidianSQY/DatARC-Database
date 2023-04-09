#!/usr/bin/env python
# coding: utf-8

# In[1]:


import datarc_basic as pj
import numpy as np
import mysql.connector
import pandas as pd


# In[2]:


def strconvert(content, isInt):
    if content == "NULL":
        return
    if isInt:
        int(content)
        return str(content)
    else:
        return str(content)


# In[11]:


def onepiece(i, mycursor, csv):
    data = csv.iloc[i]
    sql = "INSERT INTO list (rank_other, rank_vtarc, rank_justification, source, name, last_name, institution, title, domain, gender, topic, description, fields, key_notes, links, email, website, pub, citation, hindex, h5index, id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val0 = strconvert(data[0], True)
    val1 = strconvert(data[1], True)
    val2 = strconvert(data[2], False)
    val3 = strconvert(data[3], False)
    val4 = strconvert(data[4], False)
    val5 = strconvert(data[5], False)
    val6 = strconvert(data[6], False)
    val7 = strconvert(data[7], False)
    val8 = strconvert(data[8], False)
    val9 = strconvert(data[9], False)
    val10 = strconvert(data[10], False)
    val11 = strconvert(data[11], False)
    val12 = strconvert(data[12], False)
    val13 = strconvert(data[13], False)
    val14 = strconvert(data[14], False)
    val15 = strconvert(data[15], False)
    val16 = strconvert(data[16], False)
    val17 = strconvert(data[17], True)
    val18 = strconvert(data[18], True)
    val19 = strconvert(data[19], True)
    val20 = strconvert(data[20], True)
    val21 = strconvert(data[21], True)
    val = [val0,val1,val2,val3,val4,val5,val6,val7,val8,val9,val10,val11,val12,val13,val14,val15,val16,val17,val18,val19,val20,val21]
    mycursor.execute(sql, val)


# In[4]:


def mysql_connect(hoststr, userstr, passwordstr, databasestr):
    mydb = mysql.connector.connect(host=hoststr,
                                   user=userstr,
                                   password=passwordstr,
                                   database=databasestr)
    return mydb


# In[20]:


def xlsx_to_csv(filename, targetname):
    table = pj.readTableResearch(filename)
    output = pd.DataFrame(table)
    output.to_csv(targetname+".csv", index=False, header=True)
    return targetname+".csv"


# In[21]:


def whole_table_input(db, csv_table):
    purified = pj.readTableResearch(csv_table)
    rows = purified.shape[0]
    for i in range(rows):
        onepiece(i, db.cursor(), purified)


# In[31]:


def oneline_input(db, data):
    sql = "INSERT INTO list (rank_other, rank_vtarc, rank_justification, source, name, last_name, institution, title, domain, gender, topic, description, fields, key_notes, links, email, website, pub, citation, hindex, h5index, id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val0 = strconvert(data[0], True)
    val1 = strconvert(data[1], True)
    val2 = strconvert(data[2], False)
    val3 = strconvert(data[3], False)
    val4 = strconvert(data[4], False)
    val5 = strconvert(data[5], False)
    val6 = strconvert(data[6], False)
    val7 = strconvert(data[7], False)
    val8 = strconvert(data[8], False)
    val9 = strconvert(data[9], False)
    val10 = strconvert(data[10], False)
    val11 = strconvert(data[11], False)
    val12 = strconvert(data[12], False)
    val13 = strconvert(data[13], False)
    val14 = strconvert(data[14], False)
    val15 = strconvert(data[15], False)
    val16 = strconvert(data[16], False)
    val17 = strconvert(data[17], True)
    val18 = strconvert(data[18], True)
    val19 = strconvert(data[19], True)
    val20 = strconvert(data[20], True)
    val21 = strconvert(data[21], True)
    val = [val0,val1,val2,val3,val4,val5,val6,val7,val8,val9,val10,val11,val12,val13,val14,val15,val16,val17,val18,val19,val20,val21]
    db.cursor().execute(sql, val)


# In[32]:


def handle_input(db, rank_other, rank_vtarc, rank_justification, source, name, last_name, institution, title, domain, gender, topic, description, fields, key_notes, links, email, website, pub, citation, hindex, h5index, actualid):
    sql = "INSERT INTO list (rank_other, rank_vtarc, rank_justification, source, name, last_name, institution, title, domain, gender, topic, description, fields, key_notes, links, email, website, pub, citation, hindex, h5index, id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val0 = strconvert(rank_other, True)
    val1 = strconvert(rank_vtarc, True)
    val2 = strconvert(rank_justification, False)
    val3 = strconvert(source, False)
    val4 = strconvert(name, False)
    val5 = strconvert(last_name, False)
    val6 = strconvert(institution, False)
    val7 = strconvert(title, False)
    val8 = strconvert(domain, False)
    val9 = strconvert(gender, False)
    val10 = strconvert(topic, False)
    val11 = strconvert(description, False)
    val12 = strconvert(fields, False)
    val13 = strconvert(key_notes, False)
    val14 = strconvert(links, False)
    val15 = strconvert(email, False)
    val16 = strconvert(website, False)
    val17 = strconvert(pub, True)
    val18 = strconvert(citation, True)
    val19 = strconvert(hindex, True)
    val20 = strconvert(h5index, True)
    val21 = strconvert(actualid, True)
    val = [val0,val1,val2,val3,val4,val5,val6,val7,val8,val9,val10,val11,val12,val13,val14,val15,val16,val17,val18,val19,val20,val21]
    db.cursor().execute(sql, val)


# In[95]:


def update_rank_other_info(db, id_in_db, value):
    sql = "UPDATE vtarc.list SET rank_other = %s WHERE id = %s"
    val = [value, id_in_db]
    db.cursor().execute(sql, val)


# In[96]:


def update_rank_vtarc_info(db, id_in_db, value):
    sql = "UPDATE vtarc.list SET rank_vtarc = %s WHERE id = %s"
    val = [value, id_in_db]
    db.cursor().execute(sql, val)


# In[97]:


def update_name_info(db, id_in_db, value):
    sql = "UPDATE vtarc.list SET name = %s WHERE id = %s"
    val = [value, id_in_db]
    db.cursor().execute(sql, val)


# In[98]:


def update_last_name_info(db, id_in_db, value):
    sql = "UPDATE vtarc.list SET last_name = %s WHERE id = %s"
    val = [value, id_in_db]
    db.cursor().execute(sql, val)


# In[99]:


def update_institution_info(db, id_in_db, value):
    sql = "UPDATE vtarc.list SET institution = %s WHERE id = %s"
    val = [value, id_in_db]
    db.cursor().execute(sql, val)


# In[100]:


def update_title_info(db, id_in_db, value):
    sql = "UPDATE vtarc.list SET title = %s WHERE id = %s"
    val = [value, id_in_db]
    db.cursor().execute(sql, val)


# In[101]:


def update_domain_info(db, id_in_db, value):
    sql = "UPDATE vtarc.list SET domain = %s WHERE id = %s"
    val = [value, id_in_db]
    db.cursor().execute(sql, val)


# In[102]:


def update_gender_info(db, id_in_db, value):
    sql = "UPDATE vtarc.list SET gender = %s WHERE id = %s"
    val = [value, id_in_db]
    db.cursor().execute(sql, val)


# In[103]:


def update_topic_info(db, id_in_db, value):
    sql = "UPDATE vtarc.list SET topic = %s WHERE id = %s"
    val = [value, id_in_db]
    db.cursor().execute(sql, val)


# In[104]:


def update_description_info(db, id_in_db, value):
    sql = "UPDATE vtarc.list SET description = %s WHERE id = %s"
    val = [value, id_in_db]
    db.cursor().execute(sql, val)


# In[105]:


def update_fields_info(db, id_in_db, value):
    sql = "UPDATE vtarc.list SET fields = %s WHERE id = %s"
    val = [value, id_in_db]
    db.cursor().execute(sql, val)


# In[106]:


def update_key_notes_info(db, id_in_db, value):
    sql = "UPDATE vtarc.list SET key_notes = %s WHERE id = %s"
    val = [value, id_in_db]
    db.cursor().execute(sql, val)


# In[107]:


def update_links_info(db, id_in_db, value):
    sql = "UPDATE vtarc.list SET links = %s WHERE id = %s"
    val = [value, id_in_db]
    db.cursor().execute(sql, val)


# In[108]:


def update_email_info(db, id_in_db, value):
    sql = "UPDATE vtarc.list SET email = %s WHERE id = %s"
    val = [value, id_in_db]
    db.cursor().execute(sql, val)


# In[109]:


def update_website_info(db, id_in_db, value):
    sql = "UPDATE vtarc.list SET website = %s WHERE id = %s"
    val = [value, id_in_db]
    db.cursor().execute(sql, val)


# In[110]:


def update_pub_info(db, id_in_db, value):
    sql = "UPDATE vtarc.list SET pub = %s WHERE id = %s"
    val = [value, id_in_db]
    db.cursor().execute(sql, val)


# In[111]:


def update_hindex(db, id_in_db, value):
    sql = "UPDATE vtarc.list SET hindex = %s WHERE id = %s"
    val = [value, id_in_db]
    db.cursor().execute(sql, val)


# In[112]:


def update_h5index_info(db, id_in_db, value):
    sql = "UPDATE vtarc.list SET h5index = %s WHERE id = %s"
    val = [value, id_in_db]
    db.cursor().execute(sql, val)


# In[113]:


def update_citation_info(db, id_in_db, value):
    sql = "UPDATE vtarc.list SET citation = %s WHERE id = %s"
    val = [value, id_in_db]
    db.cursor().execute(sql, val)


# In[114]:


def update_actualid_info(db, id_in_db, value):
    sql = "UPDATE vtarc.list SET actualid = %s WHERE id = %s"
    val = [value, id_in_db]
    db.cursor().execute(sql, val)




