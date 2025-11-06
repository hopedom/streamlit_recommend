import traceback
try:
    import autointp
    print('imported autointp OK')
except Exception as e:
    print('IMPORT ERROR')
    traceback.print_exc()
    raise
