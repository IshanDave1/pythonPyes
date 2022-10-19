from csvGen.csvGenerator import FixedLength, FixedRange, FromPossibleValues, createcsv

schema = {
    "col1": FixedLength("int", {"len": 5}),
    "col2": FixedLength("float", {"len": 5}),
    "col3": FixedLength("string", {"len": 5}),
    "col4": FixedRange("int", {"lohi": (10, 15)}),
    "col5": FixedRange("float", {"lohi": (5.5, 6.7)}),
    "col6": FromPossibleValues("int", {"set": [1, 2, 3, 4, 5]}),
    "col7": FromPossibleValues("int", {"set": [1.1, 2.2, 3.3]}),
    "col8": FromPossibleValues("int", {"set": ["A", "AB"]})
}

rows = 10
fileName = "eightVals"
createcsv(rows, fileName, schema)
