import pymupdf

doc = pymupdf.open('data/www.cheng-tsui.com.pdf')
print(doc.metadata)

page = doc[0]
text = page.get_text()
print(text)

# blocks = page.get_text("blocks", sort=True)
# print(blocks)
# for block in blocks:
#     print("block #", block[5])
#     print(block, "\n")

# pgdict = page.get_text("dict")
# for block in pgdict['blocks']:
#     if(block['type']==0):
#         print("block #", block['number'])
#         for line in block['lines']:
#             print("line dir: ",line['dir'],"wmode: ", line['wmode'],"\n")
#             for span in line['spans']:
#                 print("size: ",span['size'],"font: ",span['font'],"color: ",span['color'],"\n")
#                 print("\t" ,span['text'], "\n")