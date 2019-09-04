import smartpy as sp

class Certification(sp.Contract):
    def __init__(self, certifier):
        self.init(certified=sp.BigMap(tkey=sp.taddress, tvalue=sp.string), certifier=certifier)

    @sp.entryPoint
    def certify(self, params):
        sp.verify(sp.sender==self.data.certifier)
        sp.if ~self.data.certified.contains(params.address):
            self.data.certified[params.address]= params.name

@addTest(name = "Certify")
def test():
    certifier = sp.address("tz1gn1TN3gTXXWgSGKTjCSkkms78hbuaahSz")
    Contract= Certification(certifier)
    html=Contract.fullHtml()

    html+=Contract.certify(address=sp.address("tz1W4W2yFAHz7iGyQvFys4K7Df9mZL6cSKCp"), name="Yassine Amor").run(sender=certifier).html()
    setOutput(html)