struct SymbolicEntropyGraph: View {
    var entropyData: [Float]
    var body: some View {
        VStack {
            Text("Ψ Symbolic Divergence")
            Chart {
                ForEach(entropyData.indices, id: \.self) { i in
                    LineMark(x: .value("Step", i), y: .value("Entropy", entropyData[i]))
                }
            }
            .frame(height: 200)
        }
    }
}
