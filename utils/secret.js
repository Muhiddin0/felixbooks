import md5 from "md5";
export const Secret = (method, path, body, secret) => {
  return md5(method + path + body + secret);
};
