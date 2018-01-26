from YoBit import YoBit

def formated_info(yo):
    print "in formated_info"
    info = yo.info()
    for key, subkey in info.iteritems():
        if key == 'pairs':
            for key2, val in subkey.iteritems():
                print key2, " - ", val, "\n"
        else:
            print key, " - ", subkey

            # for i in info:
            # print i , " - ", info[i]
    print "end!"


def formated_ticker(yo, pair):
    print "in formated_ticker"
    ticker = yo.ticker(pair)
    for key, val in ticker[pair].iteritems():
        print key, " - ", val, "\n"


def formated_depth(yo, pair):
    print "in formated_depth"
    ticker = yo.depth(pair)
    for key, val in ticker[pair].iteritems():
        print key, " - ", val, "\n"


def main():
    pair = "dcr_btc"
    yo = YoBit()
    #formated_info(yo)
    #formated_ticker(yo,pair)
    formated_depth(yo, pair)
    pass



if __name__ == '__main__':
    main()
