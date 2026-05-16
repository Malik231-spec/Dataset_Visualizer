export default function DatasetProfilerApp() {
  return (
    <div className="min-h-screen bg-slate-100 p-6">
      <div className="max-w-6xl mx-auto">
        <div className="bg-white rounded-3xl shadow-2xl p-8 border border-slate-200">
          <div className="flex items-center justify-between mb-8">
            <div>
              <h1 className="text-4xl font-black text-slate-800">
                AI Dataset Profiler 🚀
              </h1>
              <p className="text-slate-500 mt-2 text-lg">
                Upload CSV, Excel, JSON & generate smart profiling reports.
              </p>
            </div>

            <button className="px-5 py-3 bg-indigo-600 text-white rounded-2xl font-bold hover:bg-indigo-700 transition-all">
              Dark Mode 🌙
            </button>
          </div>

          {/* Drag Drop Area */}
          <div className="border-4 border-dashed border-indigo-300 bg-indigo-50 rounded-3xl p-14 text-center hover:bg-indigo-100 transition-all cursor-pointer">
            <div className="text-6xl mb-4">📂</div>
            <h2 className="text-2xl font-bold text-slate-700 mb-2">
              Drag & Drop Dataset Here
            </h2>
            <p className="text-slate-500 mb-6">
              Supports CSV, XLSX, JSON, TXT
            </p>

            <input
              type="file"
              className="hidden"
              id="fileUpload"
              accept=".csv,.xlsx,.json,.txt"
            />

            <label
              htmlFor="fileUpload"
              className="inline-block px-6 py-3 bg-indigo-600 text-white rounded-2xl font-bold cursor-pointer hover:bg-indigo-700"
            >
              Choose File
            </label>
          </div>

          {/* Features Grid */}
          <div className="grid md:grid-cols-3 gap-6 mt-10">
            <div className="bg-slate-50 p-6 rounded-3xl border border-slate-200 hover:shadow-xl transition-all">
              <div className="text-4xl mb-3">📊</div>
              <h3 className="text-xl font-bold mb-2">Smart Reports</h3>
              <p className="text-slate-500">
                Generate beautiful automated profiling reports instantly.
              </p>
            </div>

            <div className="bg-slate-50 p-6 rounded-3xl border border-slate-200 hover:shadow-xl transition-all">
              <div className="text-4xl mb-3">🤖</div>
              <h3 className="text-xl font-bold mb-2">AI Insights</h3>
              <p className="text-slate-500">
                Detect missing values, outliers, trends & correlations.
              </p>
            </div>

            <div className="bg-slate-50 p-6 rounded-3xl border border-slate-200 hover:shadow-xl transition-all">
              <div className="text-4xl mb-3">⚡</div>
              <h3 className="text-xl font-bold mb-2">Fast Processing</h3>
              <p className="text-slate-500">
                Optimized backend for large datasets and multiple formats.
              </p>
            </div>
          </div>

          {/* Advanced Features */}
          <div className="mt-12 bg-gradient-to-r from-indigo-600 to-violet-600 rounded-3xl p-8 text-white">
            <h2 className="text-3xl font-black mb-6">
              Extra Features 🔥
            </h2>

            <div className="grid md:grid-cols-2 gap-5 text-lg">
              <div>✅ Drag & Drop Upload</div>
              <div>✅ CSV / Excel / JSON / TXT Support</div>
              <div>✅ Auto Graph Generation</div>
              <div>✅ Correlation Heatmaps</div>
              <div>✅ Missing Value Detection</div>
              <div>✅ Download HTML Reports</div>
              <div>✅ AI Dataset Summary</div>
              <div>✅ Dark / Light Mode</div>
              <div>✅ Search & Filter Columns</div>
              <div>✅ Responsive UI</div>
            </div>
          </div>

          {/* Backend Code Preview */}
          <div className="mt-12 bg-slate-900 text-green-400 rounded-3xl p-6 overflow-auto">
            <h2 className="text-white text-2xl font-bold mb-4">
              Flask Backend Example
            </h2>

            <pre className="text-sm whitespace-pre-wrap">
{`from flask import Flask, request, jsonify
import pandas as pd
from ydata_profiling import ProfileReport
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    if file.filename.endswith('.csv'):
        df = pd.read_csv(filepath)

    elif file.filename.endswith('.xlsx'):
        df = pd.read_excel(filepath)

    elif file.filename.endswith('.json'):
        df = pd.read_json(filepath)

    else:
        return jsonify({'error':'Unsupported file'})

    profile = ProfileReport(df, title='Dataset Report')
    profile.to_file('templates/report.html')

    return jsonify({'message':'Report Generated'})

if __name__ == '__main__':
    app.run(debug=True)
`}
            </pre>
          </div>

          {/* Footer */}
          <div className="text-center mt-10 text-slate-400 text-sm">
            Built with React + Flask + Pandas Profiling ❤️
          </div>
        </div>
      </div>
    </div>
  )
}
