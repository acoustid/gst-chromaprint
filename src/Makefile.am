# Note: plugindir is set in configure

plugin_LTLIBRARIES = libgstchromaprint.la

# sources used to compile this plug-in
libgstchromaprint_la_SOURCES = gstchromaprint.c gstchromaprint.h

# compiler and linker flags used to compile this plugin, set in configure.ac
libgstchromaprint_la_CFLAGS = $(GST_CFLAGS) $(CHROMAPRINT_CFLAGS)
libgstchromaprint_la_LIBADD = $(GST_LIBS) $(CHROMAPRINT_LIBS)
libgstchromaprint_la_LDFLAGS = $(GST_PLUGIN_LDFLAGS)
libgstchromaprint_la_LIBTOOLFLAGS = --tag=disable-static

# headers we need but don't want installed
noinst_HEADERS = gstchromaprint.h
