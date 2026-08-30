const fs = require('fs');
const path = require('path');
const { createClient } = require('@supabase/supabase-js');

// Parse .env.local
const envPath = path.join(__dirname, '..', 'butterfly-app', '.env.local');
const envContent = fs.readFileSync(envPath, 'utf8');
const env = {};
envContent.split('\n').forEach(line => {
  const parts = line.trim().split('=');
  if (parts.length >= 2) {
    env[parts[0].trim()] = parts.slice(1).join('=').trim();
  }
});

const supabaseUrl = env.NEXT_PUBLIC_SUPABASE_URL;
const supabaseAnonKey = env.NEXT_PUBLIC_SUPABASE_ANON_KEY;

console.log("Supabase URL:", supabaseUrl);
console.log("Supabase Anon Key length:", supabaseAnonKey ? supabaseAnonKey.length : 0);

const supabase = createClient(supabaseUrl, supabaseAnonKey);

async function run() {
  try {
    const { data: species, error: spError } = await supabase
      .from('spesies')
      .select('id, nama_umum');
      
    if (spError) throw spError;
    console.log("Loaded species:", species.length);
    
    const { data: performance, error: perfError } = await supabase
      .from('performa_model')
      .select('id, spesies_id, jumlah_benar, jumlah_total, avg_confidence');
      
    if (perfError) throw perfError;
    console.log("Loaded performance records:", performance.length);
    if (performance.length > 0) {
      console.log("Sample performance record:", performance[0]);
    }
  } catch (err) {
    console.error("Error:", err);
  }
}

run();
