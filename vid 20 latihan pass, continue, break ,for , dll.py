#a = 10
#count = 1
#for i in range(a):
    #print('*'*count)
    #count +=  1 
a=11
kucing= "* "*13
mata_kucing = ("* "*4 + " "*10 + "* "*4)*2
mata_kucingkiri = " * "*3
spasi = a
count =  1 
while True:
    print(" "*spasi,"* "*count," "*spasi*2, "* "*count) 
    count +=  1
    spasi -= 1
    if count > a:
        print(f"""{kucing*2}\n{kucing*2}\n{kucing*2}\n{kucing*2}\n{mata_kucing}\n{mata_kucing}\n{mata_kucing}\n{kucing*2}\n{kucing*2}""")

        break
    elif spasi < 0:
        
        break
print("""
* * * * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * * * *       *   
* * * * * * * * * * * * * * * * * * * * *   * *
* * *         * * * * * *         * * * *  *
* * *         * * * * * *         * * * **
* * *         * * * * * *         * * * * * * *  *
* * * * * * * * * * * * * * * * * * * * *  *      * *
* * * * * * * *           * * * * * * * *    *       *
* * * * * * * * *       * * * * * * * * *      *
* * * * * * * * * *   * * * * * * * * * * 
* * * * * * * * *     * * * * * * * * * *
* * *   * * * *   * *   * * * * *   * * *
* * * *   * * *   * * *   * * *   * * * *
* * * * *       * * * * *        * * * *
* * * * * * * * * * * * * * * * * * * * *
""")