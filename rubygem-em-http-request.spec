#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-em-http-request
Version  : 1.1.2
Release  : 1
URL      : https://rubygems.org/downloads/em-http-request-1.1.2.gem
Source0  : https://rubygems.org/downloads/em-http-request-1.1.2.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-addressable
BuildRequires : rubygem-bundler
BuildRequires : rubygem-cookiejar
BuildRequires : rubygem-devise
BuildRequires : rubygem-diff-lcs
BuildRequires : rubygem-em-socksify
BuildRequires : rubygem-eventmachine
BuildRequires : rubygem-multi_json
BuildRequires : rubygem-rack
BuildRequires : rubygem-rake
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-rspec
BuildRequires : rubygem-rspec-core
BuildRequires : rubygem-rspec-expectations
BuildRequires : rubygem-rspec-mocks
BuildRequires : rubygem-rspec-support

%description
# EM-HTTP-Request
Async (EventMachine) HTTP client, with support for:
- Asynchronous HTTP API for single & parallel request execution
- Keep-Alive and HTTP pipelining support
- Auto-follow 3xx redirects with max depth
- Automatic gzip & deflate decoding
- Streaming response processing
- Streaming file uploads
- HTTP proxy and SOCKS5 support
- Basic Auth & OAuth
- Connection-level & Global middleware support
- HTTP parser via [http_parser.rb](https://github.com/tmm1/http_parser.rb)
- Works wherever EventMachine runs: Rubinius, JRuby, MRI

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n em-http-request-1.1.2
gem spec %{SOURCE0} -l --ruby > rubygem-em-http-request.gemspec

%build
gem build rubygem-em-http-request.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
em-http-request-1.1.2.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.2.0/cache/em-http-request-1.1.2.gem
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HTTPMethods/cdesc-HTTPMethods.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HTTPMethods/delete-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HTTPMethods/get-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HTTPMethods/head-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HTTPMethods/options-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HTTPMethods/patch-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HTTPMethods/post-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HTTPMethods/put-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpClient/CookieJar/cdesc-CookieJar.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpClient/CookieJar/get-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpClient/CookieJar/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpClient/CookieJar/set-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpClient/build_request-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpClient/cdesc-HttpClient.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpClient/close-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpClient/connection_completed-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpClient/content_charset-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpClient/continue%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpClient/cookies-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpClient/error-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpClient/finished%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpClient/headers-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpClient/last_effective_url-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpClient/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpClient/normalize_body-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpClient/on_body_data-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpClient/on_decoded_body_data-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpClient/on_error-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpClient/on_request_complete-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpClient/parse_response_header-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpClient/peer-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpClient/redirect%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpClient/redirects-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpClient/req-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpClient/reset%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpClient/response-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpClient/response_header-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpClient/send_request-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpClient/state-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpClient/stream-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpClient/unbind-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpConnection/activate_connection-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpConnection/cdesc-HttpConnection.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpConnection/client-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpConnection/close-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpConnection/conn%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpConnection/conn-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpConnection/connection_completed-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpConnection/connopts-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpConnection/deferred-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpConnection/error-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpConnection/finalize_request-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpConnection/middleware-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpConnection/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpConnection/peer-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpConnection/post_init-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpConnection/receive_data-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpConnection/redirect-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpConnection/send_data-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpConnection/setup_request-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpConnection/start-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpConnection/stream_file_data-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpConnection/unbind-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpConnection/uri-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpConnection/use-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpDecoders/Base/%3c%3c-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpDecoders/Base/cdesc-Base.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpDecoders/Base/decompress-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpDecoders/Base/encoding_names-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpDecoders/Base/finalize%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpDecoders/Base/finalize-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpDecoders/Base/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpDecoders/Base/receive_decompressed-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpDecoders/DecoderError/cdesc-DecoderError.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpDecoders/Deflate/cdesc-Deflate.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpDecoders/Deflate/decompress-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpDecoders/Deflate/finalize-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpDecoders/GZip/cdesc-GZip.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpDecoders/GZip/decompress-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpDecoders/GZip/encoding_names-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpDecoders/GZip/finalize-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpDecoders/GZipHeader/cdesc-GZipHeader.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpDecoders/GZipHeader/eof%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpDecoders/GZipHeader/extract_stream-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpDecoders/GZipHeader/finished%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpDecoders/GZipHeader/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpDecoders/GZipHeader/read-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpDecoders/GZipHeader/readbyte-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpDecoders/accepted_encodings-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpDecoders/cdesc-HttpDecoders.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpDecoders/decoder_for_encoding-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpEncoding/bytesize-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpEncoding/cdesc-HttpEncoding.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpEncoding/encode_auth-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpEncoding/encode_cookie-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpEncoding/encode_field-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpEncoding/encode_headers-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpEncoding/encode_host-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpEncoding/encode_param-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpEncoding/encode_query-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpEncoding/encode_request-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpEncoding/escape-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpEncoding/form_encode_body-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpEncoding/munge_header_keys-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpEncoding/unescape-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpRequest/cdesc-HttpRequest.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpRequest/middleware-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpRequest/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpRequest/use-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpResponseHeader/%5b%5d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpResponseHeader/cdesc-HttpResponseHeader.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpResponseHeader/chunked_encoding%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpResponseHeader/client_error%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpResponseHeader/compressed%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpResponseHeader/content_length-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpResponseHeader/cookie-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpResponseHeader/etag-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpResponseHeader/http_reason-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpResponseHeader/http_status-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpResponseHeader/http_version-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpResponseHeader/informational%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpResponseHeader/keepalive%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpResponseHeader/last_modified-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpResponseHeader/location-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpResponseHeader/raw-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpResponseHeader/redirection%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpResponseHeader/server_error%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpResponseHeader/status-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpResponseHeader/successful%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpStatus/cdesc-HttpStatus.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpStubConnection/cdesc-HttpStubConnection.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpStubConnection/connection_completed-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpStubConnection/parent%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpStubConnection/parent-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpStubConnection/receive_data-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/HttpStubConnection/unbind-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/Middleware/DigestAuth/auth_digest-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/Middleware/DigestAuth/build_auth_digest-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/Middleware/DigestAuth/cdesc-DigestAuth.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/Middleware/DigestAuth/get_params-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/Middleware/DigestAuth/is_digest_auth-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/Middleware/DigestAuth/make_cnonce-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/Middleware/DigestAuth/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/Middleware/DigestAuth/next_nonce-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/Middleware/DigestAuth/request-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/Middleware/DigestAuth/response-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/Middleware/JSONResponse/cdesc-JSONResponse.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/Middleware/JSONResponse/response-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/Middleware/OAuth/cdesc-OAuth.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/Middleware/OAuth/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/Middleware/OAuth/request-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/Middleware/OAuth2/access_token-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/Middleware/OAuth2/cdesc-OAuth2.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/Middleware/OAuth2/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/Middleware/OAuth2/request-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/Middleware/OAuth2/update_uri%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/Middleware/cdesc-Middleware.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/MultiRequest/add-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/MultiRequest/cdesc-MultiRequest.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/MultiRequest/check_progress-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/MultiRequest/finished%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/MultiRequest/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/MultiRequest/requests-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/MultiRequest/responses-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/EventMachine/cdesc-EventMachine.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/HttpClientOptions/body-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/HttpClientOptions/cdesc-HttpClientOptions.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/HttpClientOptions/decoding-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/HttpClientOptions/file-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/HttpClientOptions/follow_redirect%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/HttpClientOptions/followed-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/HttpClientOptions/headers-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/HttpClientOptions/host-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/HttpClientOptions/keepalive-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/HttpClientOptions/method-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/HttpClientOptions/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/HttpClientOptions/no_body%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/HttpClientOptions/pass_cookies-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/HttpClientOptions/path-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/HttpClientOptions/port-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/HttpClientOptions/query-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/HttpClientOptions/redirects-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/HttpClientOptions/set_uri-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/HttpClientOptions/ssl%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/HttpClientOptions/uri-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/HttpConnectionOptions/bind-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/HttpConnectionOptions/bind_port-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/HttpConnectionOptions/cdesc-HttpConnectionOptions.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/HttpConnectionOptions/connect_proxy%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/HttpConnectionOptions/connect_timeout-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/HttpConnectionOptions/host-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/HttpConnectionOptions/http_proxy%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/HttpConnectionOptions/inactivity_timeout-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/HttpConnectionOptions/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/HttpConnectionOptions/port-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/HttpConnectionOptions/proxy-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/HttpConnectionOptions/socks_proxy%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/HttpConnectionOptions/tls-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/String/bytesize-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/String/cdesc-String.ri
/usr/lib64/ruby/gems/2.2.0/doc/em-http-request-1.1.2/ri/cache.ri
/usr/lib64/ruby/gems/2.2.0/gems/em-http-request-1.1.2/.gemtest
/usr/lib64/ruby/gems/2.2.0/gems/em-http-request-1.1.2/.gitignore
/usr/lib64/ruby/gems/2.2.0/gems/em-http-request-1.1.2/.rspec
/usr/lib64/ruby/gems/2.2.0/gems/em-http-request-1.1.2/Changelog.md
/usr/lib64/ruby/gems/2.2.0/gems/em-http-request-1.1.2/Gemfile
/usr/lib64/ruby/gems/2.2.0/gems/em-http-request-1.1.2/README.md
/usr/lib64/ruby/gems/2.2.0/gems/em-http-request-1.1.2/Rakefile
/usr/lib64/ruby/gems/2.2.0/gems/em-http-request-1.1.2/benchmarks/clients.rb
/usr/lib64/ruby/gems/2.2.0/gems/em-http-request-1.1.2/benchmarks/em-excon.rb
/usr/lib64/ruby/gems/2.2.0/gems/em-http-request-1.1.2/benchmarks/em-profile.gif
/usr/lib64/ruby/gems/2.2.0/gems/em-http-request-1.1.2/benchmarks/em-profile.txt
/usr/lib64/ruby/gems/2.2.0/gems/em-http-request-1.1.2/benchmarks/server.rb
/usr/lib64/ruby/gems/2.2.0/gems/em-http-request-1.1.2/em-http-request.gemspec
/usr/lib64/ruby/gems/2.2.0/gems/em-http-request-1.1.2/examples/.gitignore
/usr/lib64/ruby/gems/2.2.0/gems/em-http-request-1.1.2/examples/digest_auth/client.rb
/usr/lib64/ruby/gems/2.2.0/gems/em-http-request-1.1.2/examples/digest_auth/server.rb
/usr/lib64/ruby/gems/2.2.0/gems/em-http-request-1.1.2/examples/fetch.rb
/usr/lib64/ruby/gems/2.2.0/gems/em-http-request-1.1.2/examples/fibered-http.rb
/usr/lib64/ruby/gems/2.2.0/gems/em-http-request-1.1.2/examples/multi.rb
/usr/lib64/ruby/gems/2.2.0/gems/em-http-request-1.1.2/examples/oauth-tweet.rb
/usr/lib64/ruby/gems/2.2.0/gems/em-http-request-1.1.2/examples/socks5.rb
/usr/lib64/ruby/gems/2.2.0/gems/em-http-request-1.1.2/lib/em-http-request.rb
/usr/lib64/ruby/gems/2.2.0/gems/em-http-request-1.1.2/lib/em-http.rb
/usr/lib64/ruby/gems/2.2.0/gems/em-http-request-1.1.2/lib/em-http/client.rb
/usr/lib64/ruby/gems/2.2.0/gems/em-http-request-1.1.2/lib/em-http/core_ext/bytesize.rb
/usr/lib64/ruby/gems/2.2.0/gems/em-http-request-1.1.2/lib/em-http/decoders.rb
/usr/lib64/ruby/gems/2.2.0/gems/em-http-request-1.1.2/lib/em-http/http_client_options.rb
/usr/lib64/ruby/gems/2.2.0/gems/em-http-request-1.1.2/lib/em-http/http_connection.rb
/usr/lib64/ruby/gems/2.2.0/gems/em-http-request-1.1.2/lib/em-http/http_connection_options.rb
/usr/lib64/ruby/gems/2.2.0/gems/em-http-request-1.1.2/lib/em-http/http_encoding.rb
/usr/lib64/ruby/gems/2.2.0/gems/em-http-request-1.1.2/lib/em-http/http_header.rb
/usr/lib64/ruby/gems/2.2.0/gems/em-http-request-1.1.2/lib/em-http/http_status_codes.rb
/usr/lib64/ruby/gems/2.2.0/gems/em-http-request-1.1.2/lib/em-http/middleware/digest_auth.rb
/usr/lib64/ruby/gems/2.2.0/gems/em-http-request-1.1.2/lib/em-http/middleware/json_response.rb
/usr/lib64/ruby/gems/2.2.0/gems/em-http-request-1.1.2/lib/em-http/middleware/oauth.rb
/usr/lib64/ruby/gems/2.2.0/gems/em-http-request-1.1.2/lib/em-http/middleware/oauth2.rb
/usr/lib64/ruby/gems/2.2.0/gems/em-http-request-1.1.2/lib/em-http/multi.rb
/usr/lib64/ruby/gems/2.2.0/gems/em-http-request-1.1.2/lib/em-http/request.rb
/usr/lib64/ruby/gems/2.2.0/gems/em-http-request-1.1.2/lib/em-http/version.rb
/usr/lib64/ruby/gems/2.2.0/gems/em-http-request-1.1.2/spec/client_fiber_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/em-http-request-1.1.2/spec/client_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/em-http-request-1.1.2/spec/digest_auth_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/em-http-request-1.1.2/spec/dns_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/em-http-request-1.1.2/spec/encoding_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/em-http-request-1.1.2/spec/external_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/em-http-request-1.1.2/spec/fixtures/google.ca
/usr/lib64/ruby/gems/2.2.0/gems/em-http-request-1.1.2/spec/fixtures/gzip-sample.gz
/usr/lib64/ruby/gems/2.2.0/gems/em-http-request-1.1.2/spec/gzip_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/em-http-request-1.1.2/spec/helper.rb
/usr/lib64/ruby/gems/2.2.0/gems/em-http-request-1.1.2/spec/http_proxy_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/em-http-request-1.1.2/spec/middleware/oauth2_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/em-http-request-1.1.2/spec/middleware_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/em-http-request-1.1.2/spec/multi_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/em-http-request-1.1.2/spec/pipelining_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/em-http-request-1.1.2/spec/redirect_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/em-http-request-1.1.2/spec/socksify_proxy_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/em-http-request-1.1.2/spec/ssl_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/em-http-request-1.1.2/spec/stallion.rb
/usr/lib64/ruby/gems/2.2.0/gems/em-http-request-1.1.2/spec/stub_server.rb
/usr/lib64/ruby/gems/2.2.0/specifications/em-http-request-1.1.2.gemspec
