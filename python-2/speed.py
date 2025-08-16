import time
def hesaplama(fn):
    def inner(*args,**kwargs):
        start_time = time.perf_counter() # -> hesaplama işlemi için
        print(f"{fn.__name__} metodu çalıştırılıyor")
        result = fn(*args,**kwargs)
        end_time = time.perf_counter() # -> hesaplama işlemi için
        run_time = end_time - start_time # -> ikisinin farkı ile geçen süreyi bulma işlemi 
        print(f"geçen süre : {run_time}")
        return result
    return inner
@hesaplama
def sum_gen():
    return sum((x for x in range(100000)))
@hesaplama
def sum_list():
    return sum([x for x in range(100000)])
    
print(sum_gen())
print(sum_list())