// TEST FILE for TestNexus header check — fake values only, delete after testing....
fetch('/api/data', {
  headers: {
    Authorization: 'Bearer eyJhbGciOiJIUzI1NiJ9.FAKE.TOKEN123456',
    'X-Password': userPassword,
  },
});

axios.post('/api/save', data, { headers: { 'X-API-Key': 'FAKEKEY1234567890abcdef' } });

fetch('/api/login', { headers: { Authorization: 'Basic ' + btoa('admin:fake123') } });

fetch('/api/items?api_key=' + key);
