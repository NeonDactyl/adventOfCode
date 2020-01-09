using System;
using System.Security.Cryptography;
using System.Text;

namespace cs
{
    class Program
    {
		static string GetMd5Hash(MD5 md5Hash, string input)
	        {
				byte[] data = md5Hash.ComputeHash(Encoding.UTF8.GetBytes(input));
				
				StringBuilder sBuilder = new StringBuilder();
				for (int i = 0; i < data.Length; i++)
				{
					sBuilder.Append(data[i].ToString("x2"));
				}
				return sBuilder.ToString();
			}

        static void Main(string[] args)
        {
			string input = "bgvyzdsv";
			bool notfound = true;
			int num = 0;
			while (notfound) {
				using(MD5 md5Hash = MD5.Create())
				{
					string hash = GetMd5Hash(md5Hash, input + num.ToString());
					if (hash.Substring(0, 6) == "000000") notfound = false;
				}
				num++;
			}
			Console.WriteLine(num);
        }
    }
}
