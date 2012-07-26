package XMLRPC::Transport::HTTP::Server;

use strict;

=head1 NAME

XMLRPC::Transport::HTTP::Server - XMLRPC::Lite HTTP Server

=head1 VERSION

Version 0.1

=cut

use XMLRPC::Lite;

use XMLRPC::Transport::HTTP;

@XMLRPC::Transport::HTTP::Server::ISA = qw(SOAP::Transport::HTTP::Server);

our $VERSION = '0.1';

=head1 SYNOPSIS

...

=head1 SUBROUTINES/METHODS

=head2 function1

=cut

sub initialize; *initialize = \&XMLRPC::Server::initialize;
sub make_fault; *make_fault = \&XMLRPC::Transport::HTTP::CGI::make_fault;
sub make_response; *make_response = \&XMLRPC::Transport::HTTP::CGI::make_response;

=head1 AUTHOR

Jerry Lundström, C<< <lundstrom.jerry at gmail.com> >>

=head1 BUGS

Please report any bugs or feature requests to C<bug-lim at rt.cpan.org>, or through
the web interface at L<http://rt.cpan.org/NoAuth/ReportBug.html?Queue=XMLRPC::Transport::HTTP::Server>.  I will be notified, and then you'll
automatically be notified of progress on your bug as I make changes.




=head1 SUPPORT

You can find documentation for this module with the perldoc command.

    perldoc XMLRPC::Transport::HTTP::Server


You can also look for information at:

=over 4

=item * RT: CPAN's request tracker (report bugs here)

L<http://rt.cpan.org/NoAuth/Bugs.html?Dist=XMLRPC::Transport::HTTP::Server>

=item * AnnoCPAN: Annotated CPAN documentation

L<http://annocpan.org/dist/XMLRPC::Transport::HTTP::Server>

=item * CPAN Ratings

L<http://cpanratings.perl.org/d/XMLRPC::Transport::HTTP::Server>

=item * Search CPAN

L<http://search.cpan.org/dist/XMLRPC::Transport::HTTP::Server/>

=back


=head1 ACKNOWLEDGEMENTS


=head1 LICENSE AND COPYRIGHT

Copyright 2012 Jerry Lundström.

This program is free software; you can redistribute it and/or modify it
under the terms of either: the GNU General Public License as published
by the Free Software Foundation; or the Artistic License.

See http://dev.perl.org/licenses/ for more information.


=cut

1; # End of XMLRPC::Transport::HTTP::Server
